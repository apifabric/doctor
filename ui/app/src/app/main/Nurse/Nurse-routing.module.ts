import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NurseHomeComponent } from './home/Nurse-home.component';
import { NurseNewComponent } from './new/Nurse-new.component';
import { NurseDetailComponent } from './detail/Nurse-detail.component';

const routes: Routes = [
  {path: '', component: NurseHomeComponent},
  { path: 'new', component: NurseNewComponent },
  { path: ':id', component: NurseDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Nurse-detail-permissions'
      }
    }
  }
];

export const NURSE_MODULE_DECLARATIONS = [
    NurseHomeComponent,
    NurseNewComponent,
    NurseDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NurseRoutingModule { }