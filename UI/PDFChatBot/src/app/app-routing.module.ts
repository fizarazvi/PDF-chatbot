import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UpPdfComponent } from './up-pdf/up-pdf.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
import { ArchitectureComponent } from './architecture/architecture.component';

const routes: Routes = [
    { path: '', redirectTo: '/architecture', pathMatch: 'full'},
    { path: 'architecture', component: ArchitectureComponent },
    { path: 'upload', component: UpPdfComponent },
    { path: 'chatbot', component: ChatbotComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes,{useHash:true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [ArchitectureComponent, UpPdfComponent, ChatbotComponent]
