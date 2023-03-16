import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { UsuarioService } from '../../../core/services/usuario.service';
import { AlertsService, IUsuario } from 'src/app/core/';
import { DialogUsuarioComponent } from './dialog-usuario/dialog-usuario.component';
import { MdbModalRef, MdbModalService } from 'mdb-angular-ui-kit/modal';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.css'],
})
export class UsuarioComponent implements OnInit {
  displayedColumns: string[] = [
    'id',
    'nombre',
    'apellido',
    'username',
    'usertype',
    'is_active',
    'opciones',
  ];

  public usuarios!: IUsuario[];
  dataSource = new MatTableDataSource<IUsuario>(this.usuarios);
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  public form!: FormGroup;
  private id: number | undefined;
  modalRef: MdbModalRef<
    DialogUsuarioComponent | DialogUsuarioComponent
  > | null = null;
  constructor(
    private usuarioService: UsuarioService,
    private _alertServices: AlertsService,
    private modalService: MdbModalService,
  ) {
   
  }

  ngOnInit(): void {
    this.listarUsuarios();
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }
  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  listarUsuarios(): void {
    this.usuarioService.obtenerUsuarios().subscribe((data: IUsuario[]) => {
      console.log(data);
      this.dataSource.data = data;
    });
  }
 
  modificarEstado(id: number, accion: number) {
    this.usuarioService.modificarEstadoUsuario(id, accion).subscribe({
      next: (resp) => this.listarUsuarios(),
      error: (error) => this._alertServices.alertError('A ocurrido un error'),
    });
  }
  getUserAuth(){
    return this.usuarioService.getUser();
  }


  openDialog() {
    this.modalRef = this.modalService.open(DialogUsuarioComponent, {
      modalClass: 'modal-lg',
    });
    this.modalRef.onClose.subscribe({
      next: (response: IUsuario) => {
        if (response) this.listarUsuarios();
      },
    });
  }

  openDialogForEdit(usuario: IUsuario) {
    this.modalRef = this.modalService.open(DialogUsuarioComponent, {
      modalClass: 'modal-lg',
      data: { usuarioEdit: usuario },
    });
    this.modalRef.onClose.subscribe({
      next: (response: IUsuario) => {
        if (response) this.listarUsuarios();
      },
    });
  }

  openDialogForDetail(usuario: IUsuario) {
    this.modalRef = this.modalService.open(DialogUsuarioComponent, {
      modalClass: 'modal-dialog-centered',
      data: { usuario: usuario },
    });
  }
}
