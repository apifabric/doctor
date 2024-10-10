import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TreatmentHomeComponent } from './home/Treatment-home.component';
import { TreatmentNewComponent } from './new/Treatment-new.component';
import { TreatmentDetailComponent } from './detail/Treatment-detail.component';

const routes: Routes = [
  {path: '', component: TreatmentHomeComponent},
  { path: 'new', component: TreatmentNewComponent },
  { path: ':id', component: TreatmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Treatment-detail-permissions'
      }
    }
  }
];

export const TREATMENT_MODULE_DECLARATIONS = [
    TreatmentHomeComponent,
    TreatmentNewComponent,
    TreatmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TreatmentRoutingModule { }