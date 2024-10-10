import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DepartmentHomeComponent } from './home/Department-home.component';
import { DepartmentNewComponent } from './new/Department-new.component';
import { DepartmentDetailComponent } from './detail/Department-detail.component';

const routes: Routes = [
  {path: '', component: DepartmentHomeComponent},
  { path: 'new', component: DepartmentNewComponent },
  { path: ':id', component: DepartmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Department-detail-permissions'
      }
    }
  },{
    path: ':department_id/Nurse', loadChildren: () => import('../Nurse/Nurse.module').then(m => m.NurseModule),
    data: {
        oPermission: {
            permissionId: 'Nurse-detail-permissions'
        }
    }
},{
    path: ':department_id/Room', loadChildren: () => import('../Room/Room.module').then(m => m.RoomModule),
    data: {
        oPermission: {
            permissionId: 'Room-detail-permissions'
        }
    }
}
];

export const DEPARTMENT_MODULE_DECLARATIONS = [
    DepartmentHomeComponent,
    DepartmentNewComponent,
    DepartmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DepartmentRoutingModule { }