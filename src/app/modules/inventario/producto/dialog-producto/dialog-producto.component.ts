import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

import {MdbModalRef} from 'mdb-angular-ui-kit/modal';

import {
  AlertsService,
  IProducto,
  IProveedor,
  ISede,
  ProductoService,
  ProveedorService,
  SedeService,
} from 'src/app/core';
import {Action, Store} from "@ngrx/store";
import {AppState} from "../../../../app.state";
import {productAction} from "../state/product.action";
import {Observable, take} from "rxjs";
import {selectProducts} from "../state/product.selector";
import {uploadPicture} from "../../../../utils/uploadPicture";
import {createForm} from "../form.product";

@Component({
  selector: 'app-dialog-producto',
  templateUrl: './dialog-producto.component.html',
  styleUrls: ['./dialog-producto.component.css'],
})
export class DialogProductoComponent implements OnInit {
  product$:Observable<any> = new Observable<any>();
  fileImg!:File;

  public form!: FormGroup;
  sedes: ISede[] = [];
  proveedores: IProveedor[] = [];
  productoEdit!: IProducto;
  constructor(
    private fb: FormBuilder,
    public modalRef: MdbModalRef<DialogProductoComponent>,
    private _productoService: ProductoService,
    private _sedeService: SedeService,
    private _proveedorService: ProveedorService,
    private _alertService: AlertsService,
    private store:Store<AppState>,
  ) {
    this.form = createForm();
  }

  ngOnInit(): void {
    this.product$ = this.store.select(selectProducts);
    if (this.productoEdit) {
      this.setForm();
    }
    this.listarSede();
    this.listarProveedor();
  }
  loadImage(event: any) {
    this.fileImg = event.target.files[0] as File;
  }
  async submitProduct() {
    const product: IProducto = this.form.value;
    product.image = await uploadPicture(this.fileImg);
    product.user = 1;
    if (!this.productoEdit) {
      this.addProduct(product);
    } else {
      this.updateProduct(product);
    }
  }
  private handlerProductAction(action:Action, message:string){
    this.store.dispatch(action);
    this.store.select(selectProducts).pipe(
      take(1)
    ).subscribe(()=> {
      this._alertService.alertSucces(message);
      this.form.reset();
      this.modalRef.close();
    })
  }
  private addProduct(product: IProducto) {
    this.handlerProductAction(productAction.addProduct({product}), "Producto Registrado");
  }

  private updateProduct(product: IProducto) {
    this.handlerProductAction(productAction.updateProduct({product}), "Producto Modificado");
  }

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

}
