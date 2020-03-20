import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpEventType, HttpErrorResponse } from '@angular/common/http';
import { AfterViewInit, ViewChild, ViewChildren, ElementRef,   QueryList, HostListener} from '@angular/core';
import { UploadService } from '../upload.service'

/*
  This component provides the functions
   to add messages by both bot and user
*/

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {

  question = "";
  SERVER_URL = "http://127.0.0.1:5000/";

  @ViewChild('scrollframe', {static: false}) scrollFrame: ElementRef;
  @ViewChildren('msg') messageElements: QueryList<any>;

  private messageContainer: any;
  private scrollContainer: any;
  messages = [];

  constructor(private uploadService: UploadService, private http: HttpClient){ }

  ngOnInit(): void {
    this.addBotMessage('How can I help you?');
  }

  ngAfterViewInit() {
    this.scrollContainer = this.scrollFrame.nativeElement;
    this.messageElements.changes.subscribe(_ => this.onMessagesChanged());
  }
  //whenever msg added scroll to the bottom of the chat-panel
  private onMessagesChanged() {
    this.scrollToBottom();
  }

  private scrollToBottom() {
    this.scrollContainer.scroll({
      top: this.scrollContainer.scrollHeight,
      left: 0,
      behavior: 'smooth'
    });
  }

  //when user enters the question or clicks the send button
  handleUserMessage(){
    if(this.question==""){
      return;
    }
    this.addUserMessage();
    this.uploadService.askQuestion(this.question)
                       .subscribe(res => {
                          this.addBotMessage(res.data.answer);
                       });
    this.question = "";
  }

  //adding the msg to the msg array

  addUserMessage() {
    this.messages.push({
      text: this.question,
      sender: 'You',
      reply: false,
      date: new Date()
    });
  }

  addBotMessage(text) {
    this.messages.push({
      text: text,
      sender: 'Bot',
      reply: true,
      date: new Date()
    });
  }

}
