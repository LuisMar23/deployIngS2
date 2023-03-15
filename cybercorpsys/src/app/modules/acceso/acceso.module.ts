import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from 'src/app/shared/shared.module';
import { ReactiveFormsModule } from '@angular/forms';

import { AccesoRoutingModule } from './acceso-routing.module';
import { UsuarioComponent } from './usuario/usuario.component';
import { RolComponent } from './rol/rol.component';
import { PermisosComponent } from './permisos/permisos.component';
import { DataTablesModule } from 'angular-datatables';




@NgModule({
  declarations: [
    UsuarioComponent,
    RolComponent,
    PermisosComponent
  ],
  imports: [
    CommonModule,
    AccesoRoutingModule,
    ReactiveFormsModule,
    SharedModule,
    DataTablesModule
  ]
})
export class AccesoModule { }
