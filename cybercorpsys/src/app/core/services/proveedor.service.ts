import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { map, Observable, tap } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IProveedor } from '../interfaces/proveedor';
import { IResponse } from '../interfaces/response';

@Injectable({
  providedIn: 'root',
})
export class ProveedorService {
  public cantidadProveedor:number = 0;
  constructor(
    private httpClient: HttpClient,
    private cookieService: CookieService
  ) {}

  listarProveedores(): Observable<IProveedor[]> {
    return this.httpClient
      .get<IProveedor[]>(`${environment.API_URL}/inventario/proveedor/`, {headers:this.getHeaders()});
  }
  agregarProveedor(proveedor: IProveedor): Observable<IProveedor> {
    return this.httpClient.post<IProveedor>(
      `${environment.API_URL}/inventario/proveedor/`,
      proveedor,
      { headers: this.getHeaders() }
    );
  }

  editarProveedor(proveedor: IProveedor): Observable<IProveedor> {
    return this.httpClient.put<IProveedor>(
      `${environment.API_URL}/inventario/proveedor/${proveedor.id}/`,
      proveedor,
      { headers: this.getHeaders() }
    );
  }
  modificarEstadoProveedor(id: number, accion: number): Observable<any> {
    return this.httpClient.delete(
      `${environment.API_URL}/inventario/proveedor/${id}/`,
      { headers: this.getHeaders(), params:{accion:accion} }
    );
  }
  private getHeaders():HttpHeaders{
    return new HttpHeaders({
      'content-type': 'application/json',
      Authorization: `Bearer ${this.cookieService.get('access')}`,
    });
  }
}
