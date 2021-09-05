import { Component } from '@angular/core';
import { GlobalService } from '../global.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})

export class Tab1Page {

  articleList: any[] = []
  postObj: any[] = []
  response: any[] = []

  constructor(
    public gs: GlobalService
  ) {}

  ngOnInit(){
    console.log('1')
    const body = this.postObj
    this.gs.http('https://1ff5-240f-c1-bd4e-1-983c-767a-bedb-1253.ngrok.io/output', body).subscribe(
      res=>{
        this.response = res
        if(this.response){
          this.articleList = this.response
          console.log(this.articleList)
        }
        else{
          console.log('error')
        }
      }
    )
  }
}
