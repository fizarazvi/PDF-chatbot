import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule, routingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { UpPdfComponent } from './up-pdf/up-pdf.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
import { ArchitectureComponent } from './architecture/architecture.component';

@NgModule({
  declarations: [
    AppComponent,
    UpPdfComponent,
    ChatbotComponent,
    ArchitectureComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
