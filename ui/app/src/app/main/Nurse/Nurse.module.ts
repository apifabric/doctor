import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {NURSE_MODULE_DECLARATIONS, NurseRoutingModule} from  './Nurse-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    NurseRoutingModule
  ],
  declarations: NURSE_MODULE_DECLARATIONS,
  exports: NURSE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class NurseModule { }