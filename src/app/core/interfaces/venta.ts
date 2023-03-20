import { IProducto } from "./producto";

export interface IVenta {
    id?:number,
    serial_number:number,
    price:number,
    buy_price:number,
    sale_tax:number,
    saleTotal:number,
    is_active:boolean,
    date_created:string,
    producto:IProducto
}
