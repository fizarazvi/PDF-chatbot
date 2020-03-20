import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpEventType, HttpErrorResponse } from '@angular/common/http';
import { UploadService } from '../upload.service'
import { catchError, map } from 'rxjs/operators';
import { of } from 'rxjs';

/*
  This component provides the functions to upload pdf
*/

@Component({
  selector: 'app-up-pdf',
  templateUrl: './up-pdf.component.html',
  styleUrls: ['./up-pdf.component.css']
})
export class UpPdfComponent implements OnInit {
  fileData: File = null;
  uploadedFilePath: string = null;
  constructor(private uploadService: UploadService) { }

  // get input file
  fileProgress(fileInput: any) {
      this.fileData = <File>fileInput.target.files[0];
  }

  //when submit button clicked call the upload service
  onSubmit() {
      if(this.fileData==null){
        alert("select a file");
        return;
      }
      if(this.fileData.name.length >4 && this.fileData.name.substr(-4,4)!='.pdf'){
        alert("upload only pdf");
        return;
      }

      const formData = new FormData();
      formData.append('pdf', this.fileData);

      this.uploadService.upload(formData).pipe(
      map(event => {
        console.log(event);
        switch (event.type) {
          case HttpEventType.UploadProgress:
            //file.progress = Math.round(event.loaded * 100 / event.total);
            break;
          case HttpEventType.Response:
            return event;
        }
      }),
      catchError((error: HttpErrorResponse) => {
        console.log(error)
        return of(`${this.fileData.name} upload failed.`);
      })).subscribe((event: any) => {
        if (typeof (event) === 'object') {
          console.log(event.body);
        }
      });
  }
  ngOnInit(): void {
  }

}
