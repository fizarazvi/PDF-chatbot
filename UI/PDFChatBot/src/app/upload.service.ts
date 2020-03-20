import { Injectable } from '@angular/core';
import { HttpClient, HttpEvent, HttpErrorResponse, HttpEventType } from  '@angular/common/http';
import { map } from  'rxjs/operators';

/*
  This service is used to call the api
  for uploading pdf and
  sending the question asked to the bot
*/

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  SERVER_URL: string = "http://127.0.0.1:5000/";
	constructor(private httpClient: HttpClient) { }

  public upload(formData) {

    return this.httpClient.post<any>(this.SERVER_URL+'handleUpload', formData, {
        reportProgress: true,
        observe: 'events'
      });
  }

  public askQuestion(text) {
    console.log("askQuestion");
    return this.httpClient.post<any>(this.SERVER_URL+'questions', text, {
      });
  }

}
