import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'LabTest-new',
  templateUrl: './LabTest-new.component.html',
  styleUrls: ['./LabTest-new.component.scss']
})
export class LabTestNewComponent {
  @ViewChild("LabTestForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}