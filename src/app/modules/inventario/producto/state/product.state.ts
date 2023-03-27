import {IProducto} from "../../../../core";

export interface ProductState{
  products:Array<IProducto>;
  product:IProducto | null,
  isLoading:boolean;
  error: Error | null
}
