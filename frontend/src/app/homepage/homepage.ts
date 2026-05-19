import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-homepage',
  imports: [],
  templateUrl: './homepage.html',
  styleUrl: './homepage.css',
})
export class Homepage {
  @Output() goChat = new EventEmitter<void>();
  openChat() {
    this.goChat.emit();
  }
}
