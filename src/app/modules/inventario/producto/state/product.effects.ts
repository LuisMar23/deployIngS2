import {Actions, createEffect, ofType} from "@ngrx/effects";
import {Injectable} from "@angular/core";
import {ProductoService} from "../../../../core";
import {productAction} from "./product.action";
import {catchError, exhaustMap, map} from "rxjs";

@Injectable()
export class ProductEffects {
  constructor(private actions$:Actions, private productService:ProductoService) {
  }
  loadProducts$ = createEffect(() => this.actions$.pipe(
    ofType(productAction.loadProducts),
    exhaustMap(({products}) => this.productService.listarProductos().pipe(
      map(products => ({type:productAction.loadProductsSuccess.type, products})),
    ))
  ));
  addProduct$ = createEffect(() => this.actions$.pipe(
    ofType(productAction.addProduct),
    exhaustMap(({product}) => this.productService.agregarProducto(product).pipe(
      map(product => ({type:productAction.addProductSuccess.type, product}))
    ))
  ));
}
