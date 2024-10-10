import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LabTestHomeComponent } from './home/LabTest-home.component';
import { LabTestNewComponent } from './new/LabTest-new.component';
import { LabTestDetailComponent } from './detail/LabTest-detail.component';

const routes: Routes = [
  {path: '', component: LabTestHomeComponent},
  { path: 'new', component: LabTestNewComponent },
  { path: ':id', component: LabTestDetailComponent,
    data: {
      oPermission: {
        permissionId: 'LabTest-detail-permissions'
      }
    }
  }
];

export const LABTEST_MODULE_DECLARATIONS = [
    LabTestHomeComponent,
    LabTestNewComponent,
    LabTestDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LabTestRoutingModule { }