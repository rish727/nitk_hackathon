import { Component } from '@angular/core';
import { GlobalService } from '../global.service';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {

  articleList: any[] = []
  postObj: any[] = []
  response: any[] = []

  constructor(
    public gs: GlobalService
  ) {}

  ngOnInit(){
    console.log('1')
    const body = this.postObj
    this.gs.http('https://df60-118-10-65-11.ngrok.io/output', body).subscribe(
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
