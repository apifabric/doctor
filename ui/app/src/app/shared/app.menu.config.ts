import { MenuRootItem } from 'ontimize-web-ngx';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { BillingCardComponent } from './Billing-card/Billing-card.component';

import { DepartmentCardComponent } from './Department-card/Department-card.component';

import { DoctorCardComponent } from './Doctor-card/Doctor-card.component';

import { InsuranceCardComponent } from './Insurance-card/Insurance-card.component';

import { LabTestCardComponent } from './LabTest-card/LabTest-card.component';

import { MedicalRecordCardComponent } from './MedicalRecord-card/MedicalRecord-card.component';

import { NurseCardComponent } from './Nurse-card/Nurse-card.component';

import { PatientCardComponent } from './Patient-card/Patient-card.component';

import { PrescriptionCardComponent } from './Prescription-card/Prescription-card.component';

import { RoomCardComponent } from './Room-card/Room-card.component';

import { TreatmentCardComponent } from './Treatment-card/Treatment-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'Billing', name: 'BILLING', icon: 'view_list', route: '/main/Billing' }
    
        ,{ id: 'Department', name: 'DEPARTMENT', icon: 'view_list', route: '/main/Department' }
    
        ,{ id: 'Doctor', name: 'DOCTOR', icon: 'view_list', route: '/main/Doctor' }
    
        ,{ id: 'Insurance', name: 'INSURANCE', icon: 'view_list', route: '/main/Insurance' }
    
        ,{ id: 'LabTest', name: 'LABTEST', icon: 'view_list', route: '/main/LabTest' }
    
        ,{ id: 'MedicalRecord', name: 'MEDICALRECORD', icon: 'view_list', route: '/main/MedicalRecord' }
    
        ,{ id: 'Nurse', name: 'NURSE', icon: 'view_list', route: '/main/Nurse' }
    
        ,{ id: 'Patient', name: 'PATIENT', icon: 'view_list', route: '/main/Patient' }
    
        ,{ id: 'Prescription', name: 'PRESCRIPTION', icon: 'view_list', route: '/main/Prescription' }
    
        ,{ id: 'Room', name: 'ROOM', icon: 'view_list', route: '/main/Room' }
    
        ,{ id: 'Treatment', name: 'TREATMENT', icon: 'view_list', route: '/main/Treatment' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AppointmentCardComponent

    ,BillingCardComponent

    ,DepartmentCardComponent

    ,DoctorCardComponent

    ,InsuranceCardComponent

    ,LabTestCardComponent

    ,MedicalRecordCardComponent

    ,NurseCardComponent

    ,PatientCardComponent

    ,PrescriptionCardComponent

    ,RoomCardComponent

    ,TreatmentCardComponent

];