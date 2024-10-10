import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './LabTest-card.component.html',
  styleUrls: ['./LabTest-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.LabTest-card]': 'true'
  }
})

export class LabTestCardComponent {


}