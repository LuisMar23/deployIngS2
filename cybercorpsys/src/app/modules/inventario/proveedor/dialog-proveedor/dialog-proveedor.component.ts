import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MdbModalRef } from 'mdb-angular-ui-kit/modal';
import { ProveedorService, AlertsService, IProveedor } from 'src/app/core';

@Component({
  selector: 'app-dialog-proveedor',
  templateUrl: './dialog-proveedor.component.html',
  styleUrls: ['./dialog-proveedor.component.css'],
})
export class DialogProveedorComponent implements OnInit {
  public form!: FormGroup;
  proveedorEdit !: IProveedor;
  constructor(
    private _proveedorService: ProveedorService,
    private fb: FormBuilder,
    private _alertService: AlertsService,
    public modalRef: MdbModalRef<DialogProveedorComponent>,
  ) {
    this.form = this.fb.group({
      id:[''],
      nombre: ['', Validators.required],
      contacto: ['', Validators.required],
      correo: ['', Validators.required],
      direccion: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    if(this.proveedorEdit){
      this.setForm();
    }
  }
  submitProveedor() {
    const proveedor: IProveedor = this.form.value;
    if (!this.proveedorEdit) {
      this.addProveedor(proveedor);
    } else {
      this.updateProveedor(proveedor);
    }
  }
  private addProveedor(proveedor: IProveedor) {
    this._proveedorService.agregarProveedor(proveedor).subscribe({
      next: (response) => {
        console.log(response);
        this._alertService.alertSucces('Proveedor Registrado');
        this.form.reset();
        this.modalRef.close(response);
      },
      error: (error) => {
        console.log(error);
        this._alertService.alertError('A ocurrido un error');
      },
    });
  }

  private updateProveedor(proveedor: IProveedor) {
    this._proveedorService.editarProveedor(proveedor).subscribe({
      next: (response) => {
        console.log(response);
        this._alertService.alertSucces('Proveedor Actualizado');
        this.form.reset();
        this.modalRef.close();
      },
      error: (error) => {
        console.log(error);
      },
    });
  }
  private setForm() {  
    this.form.patchValue(this.proveedorEdit);
  }
}
