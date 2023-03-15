import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { map, Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IProducto } from '../interfaces/producto';
import { IResponse } from '../interfaces/response';

@Injectable({
  providedIn: 'root',
})
export class ProductoService {
  public cantidadProductos: number = 0;
  constructor(
    private _httpClient: HttpClient,
    private _cookieService: CookieService
  ) {}



  listarProductos(): Observable<IProducto[]> {
    return this._httpClient.get<IProducto[]>(
      `${environment.API_URL}/inventario/producto/`,
      {
        headers: this.getHeaders(),
      }
    );
  }

  agregarProducto(producto: IProducto): Observable<IProducto> {
    return this._httpClient.post<IProducto>(
      `${environment.API_URL}/inventario/producto/`,
      producto,
      { headers: this.getHeaders() }
    );
  }
  modificarProducto(producto: IProducto): Observable<IProducto> {
    return this._httpClient.put<IProducto>(
      `${environment.API_URL}/inventario/producto/${producto.id}/`,
      producto,
      { headers: this.getHeaders() }
    );
  }
  modificarEstadoProducto(id: number, accion: number): Observable<any> {
    return this._httpClient.delete(
      `${environment.API_URL}/inventario/producto/${id}/`,
      { headers: this.getHeaders(), params: { accion: accion } }
    );
  }
  saveExcel(productos: IProducto[]): Observable<any> {
    return this._httpClient.post(
      `${environment.API_URL}/inventario/producto/uploadExcel/`,
      productos,
      { headers: this.getHeaders() }
    );
  }
  private getHeaders():HttpHeaders{
    return new HttpHeaders({
      'content-type': 'application/json',
      Authorization: `Bearer ${this._cookieService.get('access')}`,
    });
  }
}
