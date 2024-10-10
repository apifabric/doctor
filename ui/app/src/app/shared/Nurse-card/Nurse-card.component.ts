import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Nurse-card.component.html',
  styleUrls: ['./Nurse-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Nurse-card]': 'true'
  }
})

export class NurseCardComponent {


}