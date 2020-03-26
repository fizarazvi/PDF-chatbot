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

	constructor(private httpClient: HttpClient) { }

  public upload(formData) {

    return this.httpClient.post<any>('/handleUpload', formData, {
        reportProgress: true,
        observe: 'events'
      });
  }

  public askQuestion(formData) {
    console.log("askQuestion");
    return this.httpClient.post<any>('/questions', formData, {
      });
  }

}
