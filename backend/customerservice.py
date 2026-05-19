import json
import requests

# --- การตั้งค่า (Settings) ---
MODEL_NAME = "qwen2.5:7b"
OLLAMA_URL = "http://localhost:11434/api/chat"
CONFIG_FILE = "service_config.json"

class ServiceAgent:
    def __init__(self, config_path):
        # โหลดฐานข้อมูลความรู้ (Knowledge Base)
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                self.kb = json.load(f)
            print(f"✅ เชื่อมต่อฐานข้อมูลบริการลูกค้าสำเร็จ")
        except FileNotFoundError:
            print(f"❌ ไม่พบไฟล์ {config_path} กรุณาตรวจสอบชื่อไฟล์")
            self.kb = {}
        
        self.chat_history = []

    def call_ollama(self, messages):
        try:
            payload = {
                "model": MODEL_NAME,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": 0.3, # ตั้งค่าให้ต่ำเพื่อให้ AI ตอบแม่นยำตามข้อมูล ไม่เน้นมโน
                    "num_ctx": 4096
                }
            }
            res = requests.post(OLLAMA_URL, json=payload, timeout=60)
            return res.json()['message']['content']
        except Exception as e:
            return f"⚠️ เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {e}"

    def chat(self, user_input):
        # สร้าง System Instruction ที่เน้นเฉพาะงานบริการ
        system_instruction = f"""คุณคือเจ้าหน้าที่ฝ่ายบริการลูกค้า (Customer Service) ของร้าน TechPro Online Store
กฎการทำงาน:
1. ข้อมูลอ้างอิง: ให้ตอบคำถามโดยยึดตามนโยบายร้านนี้เท่านั้น: {json.dumps(self.kb, ensure_ascii=False)}
2. ภาษา: ตอบเป็นภาษาไทยที่สุภาพ (มีครับ/ค่ะ) และเป็นมืออาชีพ
3. ชื่อสินค้า/เทคนิค: ให้คงไว้เป็นภาษาอังกฤษตัวหนาเสมอ เช่น **iPhone 15**, **Dead Pixel**
4. การเห็นอกเห็นใจ: หากลูกค้าแจ้งว่าสินค้ามีปัญหา หรือแสดงความไม่พอใจ ให้กล่าวขออภัยและแสดงความเห็นอกเห็นใจก่อนเริ่มให้ข้อมูลการเคลม
5. ขอบเขต: ตอบเฉพาะเรื่องนโยบาย การเคลม การส่งของ และการบริการ ห้ามแนะนำการซื้อสินค้าใหม่หรือเชียร์ขายของ"""

        # เตรียม Messages (System + History + User Input)
        messages = [{"role": "system", "content": system_instruction}] + self.chat_history + [{"role": "user", "content": user_input}]

        # รับคำตอบจาก AI
        answer = self.call_ollama(messages)

        # บันทึกประวัติการคุย (เก็บ 6 ข้อความล่าสุด)
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append({"role": "assistant", "content": answer})
        if len(self.chat_history) > 6:
            self.chat_history = self.chat_history[-6:]

        return answer

# --- ส่วนการรันโปรแกรม (Main Loop) ---
if __name__ == "__main__":
    bot = ServiceAgent(CONFIG_FILE)
    
    print("\n🎧 [TechPro Customer Service] พร้อมให้บริการแล้วครับ")
    print("แจ้งปัญหาการใช้งาน, สอบถามเรื่องการเคลม หรือนโยบายร้านได้ทันที")
    print("(พิมพ์ 'exit' เพื่อออกจากแชท)\n" + "━" * 40)

    while True:
        user_query = input("👤 ลูกค้า: ")
        
        if user_query.lower() in ["exit", "quit", "ออก"]:
            print("🤖 AI: ขอบคุณที่ใช้บริการครับ ขอให้มีความสุขกับการใช้งานสินค้าครับ!")
            break
            
        if not user_query.strip():
            continue

        response = bot.chat(user_query)

        print("\n" + "─" * 20)
        print(f"🎧 AI Service: {response}")
        print("─" * 20)