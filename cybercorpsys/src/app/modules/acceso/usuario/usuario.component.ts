import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { UsuarioService } from '../../../core/services/usuario.service';
import { AlertsService, IUsuario } from 'src/app/core/';

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

  constructor(
    private usuarioService: UsuarioService,
    private fb: FormBuilder,
    private _alertServices: AlertsService
  ) {
    this.form = this.fb.group({
      nombre: ['', Validators.required],
      apellido: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required],
      usertype: ['', Validators.required],
    });
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
  registrar(): void {
    const proveedor: IUsuario = this.form.value;
    if (this.id == undefined) {
      this.usuarioService.agregarUsuario(proveedor).subscribe(
        (resp) => {
          this.listarUsuarios();
          this._alertServices.alertSucces('Usuario registrado');
          this.form.reset();
        },
        (errors) => {
          this._alertServices.alertError('A ocurrido un error');
        }
      );
    } else {
      this.id = undefined;
      // this.usuarioService.editarProveedor(proveedor, this.id).subscribe(
      //   (res) => {
      //     this.form.reset();
      //     this.id = undefined;
      //     this._alertServices.alertSucces('Proveedor modificado');
      //     this.listarProveedor();
      //   },
      //   (errors) => {
      //     console.log(errors);
      //     this._alertServices.alertError('A ocurrido un error!');
      //   }
      // );
    }
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
}
