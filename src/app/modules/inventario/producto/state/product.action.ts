import {createActionGroup, props} from "@ngrx/store";
import {IProducto} from "../../../../core";

export const productAction = createActionGroup({
  source:"product",
  events:{
    "Add Product":props<{product:IProducto}>(),
    "Add Product Success":props<{product:IProducto}>(),
    "Add Product Failure":props<{error:Error | null}>(),
    "Load Products": props<{products:Array<IProducto>}>(),
    "Load Products Success": props<{products:Array<IProducto>}>(),
    "Load Products Failure": props<{error:Error | null}>(),
  }
})
