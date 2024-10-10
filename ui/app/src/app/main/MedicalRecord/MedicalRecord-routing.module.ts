import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MedicalRecordHomeComponent } from './home/MedicalRecord-home.component';
import { MedicalRecordNewComponent } from './new/MedicalRecord-new.component';
import { MedicalRecordDetailComponent } from './detail/MedicalRecord-detail.component';

const routes: Routes = [
  {path: '', component: MedicalRecordHomeComponent},
  { path: 'new', component: MedicalRecordNewComponent },
  { path: ':id', component: MedicalRecordDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MedicalRecord-detail-permissions'
      }
    }
  },{
    path: ':medical_record_id/Treatment', loadChildren: () => import('../Treatment/Treatment.module').then(m => m.TreatmentModule),
    data: {
        oPermission: {
            permissionId: 'Treatment-detail-permissions'
        }
    }
}
];

export const MEDICALRECORD_MODULE_DECLARATIONS = [
    MedicalRecordHomeComponent,
    MedicalRecordNewComponent,
    MedicalRecordDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MedicalRecordRoutingModule { }