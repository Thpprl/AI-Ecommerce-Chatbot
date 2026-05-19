import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  // URL ของ Backend FastAPI ที่รันอยู่
  private apiUrl = 'http://127.0.0.1:8000/api/v1/chat';

  constructor(private http: HttpClient) { }

  sendMessage(message: string): Observable<any> {
    // ต้องส่งเป็น Object { message: "ข้อความ" } ตามที่ Backend กำหนดไว้ใน Schema
    return this.http.post<any>(this.apiUrl, { message: message });
  }
}