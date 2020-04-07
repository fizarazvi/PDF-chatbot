import { Component } from '@angular/core';
import { HttpClient, HttpEventType } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  styles: ['html { height: 100%; }','body { height: 100%; margin:0px;}']
})
export class AppComponent {
  title = 'PDF-chatbot';
  flagComponent = "UploadPDF";
  componentToDisplay = "Have any Questions? Ask the chatbot!";

  toggleComponent(){
    if(this.flagComponent=='UploadPDF'){
      this.flagComponent='ChatBot';
    }
  }

}
