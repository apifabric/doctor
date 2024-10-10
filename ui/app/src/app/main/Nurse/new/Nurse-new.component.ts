import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Nurse-new',
  templateUrl: './Nurse-new.component.html',
  styleUrls: ['./Nurse-new.component.scss']
})
export class NurseNewComponent {
  @ViewChild("NurseForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}