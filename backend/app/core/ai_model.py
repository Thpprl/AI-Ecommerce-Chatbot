import requests
import json
import os

class AIModel:
    def __init__(self):
        # 1. ตั้งค่าพื้นฐาน
        self.url = "http://localhost:11434/api/chat"
        self.model_name = "qwen2.5:7b" 
        
        # 2. โหลด Data (ตรวจสอบว่าไฟล์ JSON อยู่ที่ Root ของโปรเจกต์)
        self.inventory = self._load_json("category_1000_shorter.json")
        self.policies = self._load_json("service_config.json")
        
        # 3. ประวัติการสนทนา (Memory)
        self.history = []

    def _load_json(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def call_ollama(self, messages, temp=0.5):
        """ฟังก์ชันกลางสำหรับคุยกับ Ollama"""
        try:
            payload = {
                "model": self.model_name,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": temp,
                    "num_predict": 300, # ช่วยให้ตอบเร็วขึ้นโดยจำกัดความยาว
                }
            }
            res = requests.post(self.url, json=payload, timeout=60)
            return res.json()['message']['content']
        except Exception as e:
            print(f"Ollama Error: {e}")
            return "ขออภัยค่ะ ระบบขัดข้องชั่วคราว"

    def get_intent(self, user_input):
        """ยก Logic การแยก Intent มาจาก agent.py"""
        classify_prompt = f"""วิเคราะห์ประโยคลูกค้า: "{user_input}"
        ตอบสั้นๆ เพียงคำเดียวเท่านั้น:
        - ตอบ 'SERVICE' หากเป็นการแจ้งปัญหา, ของพัง, เคลม, ประกัน, การจัดส่ง หรือบ่น
        - ตอบ 'SALES' หากเป็นการถามราคา, สนใจซื้อของ, หรือขอคำแนะนำสินค้าใหม่
        """
        res = self.call_ollama([{"role": "user", "content": classify_prompt}], temp=0)
        return "SERVICE" if "SERVICE" in res.upper() else "SALES"

    def generate_response(self, user_input: str) -> str:
        # 1. วิเคราะห์โหมด (Intent)
        mode = self.get_intent(user_input)

        # 2. เตรียม System Prompt ตาม Logic ของ Agent เดิม
        if mode == "SERVICE":
            system_instruction = f"""คุณคือเจ้าหน้าที่ฝ่ายบริการลูกค้า (Customer Service)
            1. ภาษา: ตอบเป็น "ภาษาไทย" ที่สุภาพเท่านั้น ห้ามมีภาษาจีนหรืออังกฤษปน (ยกเว้นชื่อเฉพาะ)
            2. ข้อมูล: ให้ตอบตามข้อมูลนี้เท่านั้น: {json.dumps(self.policies, ensure_ascii=False)}
            3. ความแม่นยำ: ห้ามดัดแปลงตัวเลขหรือเงื่อนไขใดๆ ในข้อมูลเด็ดขาด"""
            temp = 0.2
        else:
            # --- โหมดขายสินค้า (Keyword Search แบบเดิม) ---
            stop_words = ["มี", "ไหม", "มั้ย", "ขาย", "หรือเปล่า", "ทางร้าน", "หน่อย"]
            keywords = [kw for kw in user_input.lower().split() if kw not in stop_words]
            
            matches = [i for i in self.inventory if any(kw in i.get("title", "").lower() for kw in keywords)][:3]
            stock_context = json.dumps(matches, ensure_ascii=False) if matches else "ไม่มีสินค้าที่ระบุในสต็อก"
            
            system_instruction = f"""คุณคือพนักงานขาย (Sales)
                กฎเหล็ก:
                1. ภาษา: ตอบเป็น "ภาษาไทย" เท่านั้น ห้ามมีภาษาจีนปนเด็ดขาด
                2. ข้อมูลสินค้า: แนะนำจากสต็อกนี้: {stock_context}
                3. หน่วยเงิน: **ห้ามคำนวณหรือเปลี่ยนหน่วยเงินเด็ดขาด** ให้ใช้ตัวเลขและหน่วยตามที่ระบุใน JSON เท่านั้น
                4. ชื่อสินค้า: ให้คงไว้เป็นภาษาอังกฤษตัวหนาเสมอ เช่น **Product Name**"""
            temp = 0.5

        # 3. จัดเตรียม Message (รวม History เพื่อความต่อเนื่อง)
        current_messages = [{"role": "system", "content": system_instruction}]
        # ใส่ประวัติย้อนหลัง 4 ข้อความล่าสุด
        current_messages.extend(self.history[-4:]) 
        current_messages.append({"role": "user", "content": user_input})

        # 4. เรียก AI
        answer = self.call_ollama(current_messages, temp)

        # 5. บันทึก History ไว้ใน Memory ของ Backend
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": answer})
        if len(self.history) > 6: self.history = self.history[-6:]

        return answer