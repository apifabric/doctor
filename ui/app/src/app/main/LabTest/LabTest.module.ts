import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {LABTEST_MODULE_DECLARATIONS, LabTestRoutingModule} from  './LabTest-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    LabTestRoutingModule
  ],
  declarations: LABTEST_MODULE_DECLARATIONS,
  exports: LABTEST_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class LabTestModule { }