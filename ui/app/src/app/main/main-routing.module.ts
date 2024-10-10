import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Appointment', loadChildren: () => import('./Appointment/Appointment.module').then(m => m.AppointmentModule) },
    
        { path: 'Billing', loadChildren: () => import('./Billing/Billing.module').then(m => m.BillingModule) },
    
        { path: 'Department', loadChildren: () => import('./Department/Department.module').then(m => m.DepartmentModule) },
    
        { path: 'Doctor', loadChildren: () => import('./Doctor/Doctor.module').then(m => m.DoctorModule) },
    
        { path: 'Insurance', loadChildren: () => import('./Insurance/Insurance.module').then(m => m.InsuranceModule) },
    
        { path: 'LabTest', loadChildren: () => import('./LabTest/LabTest.module').then(m => m.LabTestModule) },
    
        { path: 'MedicalRecord', loadChildren: () => import('./MedicalRecord/MedicalRecord.module').then(m => m.MedicalRecordModule) },
    
        { path: 'Nurse', loadChildren: () => import('./Nurse/Nurse.module').then(m => m.NurseModule) },
    
        { path: 'Patient', loadChildren: () => import('./Patient/Patient.module').then(m => m.PatientModule) },
    
        { path: 'Prescription', loadChildren: () => import('./Prescription/Prescription.module').then(m => m.PrescriptionModule) },
    
        { path: 'Room', loadChildren: () => import('./Room/Room.module').then(m => m.RoomModule) },
    
        { path: 'Treatment', loadChildren: () => import('./Treatment/Treatment.module').then(m => m.TreatmentModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }