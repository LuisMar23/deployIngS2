import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';

import { MdbModalRef } from 'mdb-angular-ui-kit/modal';

import {
  ProductoService,
  ProveedorService,
  SedeService,
  IProducto,
  AlertsService,
  IProveedor,
  ISede,
} from 'src/app/core';

@Component({
  selector: 'app-dialog-producto',
  templateUrl: './dialog-producto.component.html',
  styleUrls: ['./dialog-producto.component.css'],
})
export class DialogProductoComponent implements OnInit {
  public form!: FormGroup;
  sedes: ISede[] = [];
  proveedores: IProveedor[] = [];
  productoEdit!: IProducto;
  imagenBase64!: string;
  constructor(
    private fb: FormBuilder,
    private _sanitizer: DomSanitizer,
    public modalRef: MdbModalRef<DialogProductoComponent>,
    private _productoService: ProductoService,
    private _sedeService: SedeService,
    private _proveedorService: ProveedorService,
    private _alertService: AlertsService
  ) {
    //Luis Martinez RF3
    //Creaacion de un submetodo para las propiedades de producto que pueden aumentar a futuro lo que haria mas grande el codigo
    this.form = this.propProducto();
  }

  ngOnInit(): void {
    if (this.productoEdit) {
      this.setForm();
    }
    this.listarSede();
    this.listarProveedor();
  }

  submitProducto() {
    const producto: IProducto = this.form.value;
    producto.image = this.imagenBase64;
    producto.user = 1;
    if (!this.productoEdit) {
      this.addProducto(producto);
    } else {
      this.updateProducto(producto);
    }
  }

  //Luis Martinez RF2
  //Crear submetodo que recibe una imagen selecciona que sirve para codificar la imagen
  cargarImagen(event: any) {
    const fileCapture = event.target.files[0];
    this.encodeImg(fileCapture);
  }

  private addProducto(producto: IProducto) {
    this._productoService.agregarProducto(producto).subscribe({
      next: (response) => {
        console.log(response);
        this._alertService.alertSucces('Product Registrado');
        this.form.reset();
        this.modalRef.close(response);
      },
      error: (error) => {
        console.log(error);
        this._alertService.alertError('A ocurrido un error');
      },
    });
  }

  private updateProducto(producto: IProducto) {
    console.log(producto);
    this._productoService.modificarProducto(producto).subscribe({
      next: (response) => {
        console.log(response);
        this._alertService.alertSucces('Product Actualizado');
        this.form.reset();
        this.modalRef.close();
      },
      error: (error) => {
        console.log(error);
      },
    });
  }

  private encode64 = async ($event: any) =>
    new Promise((resolve, reject) => {
      try {
        const unsafeImg = window.URL.createObjectURL($event);
        const image = this._sanitizer.bypassSecurityTrustUrl(unsafeImg);
        const reader = new FileReader();
        reader.readAsDataURL($event);
        reader.onload = () => {
          resolve({
            base: reader.result,
          });
        };
        reader.onerror = (error) => {
          resolve({
            base: null,
          });
        };

      } catch (e) {}
    });

  private listarSede(): void {
    this._sedeService.listarSede().subscribe({
      next: (data) => {
        this.sedes = data.filter((sede) => sede.is_active == true);
      },
    });
  }
  private listarProveedor(): void {
    this._proveedorService.listarProveedores().subscribe({
      next: (data) => {
        this.proveedores = data.filter((proveedor) => proveedor.is_active == true);
      },
    });
  }
  private setForm() {
    this.form.patchValue(this.productoEdit);
  }
  //submetodo RF2
  private encodeImg(fileCapture:any){
    this.encode64(fileCapture).then((imagen: any) => {
      console.log(imagen);
      this.imagenBase64 = imagen.base;
    });
  }

  //Submetodo RF3
   propProducto(){
    return this.fb.group({
      id: [''],
      name: ['', Validators.required],
      description: ['', Validators.required],
      stock: ['', Validators.required],
      assurance_months: ['', Validators.required],
      industry: ['', Validators.required],
      marca: ['', Validators.required],
      purchase_price: ['', [Validators.required, Validators.min(0)]],
      selling_price: ['', [Validators.required, Validators.min(0)]],
      branchOffice: ['', Validators.required],
      supplier: ['', Validators.required],
      image: [''],
    });
  }
}
