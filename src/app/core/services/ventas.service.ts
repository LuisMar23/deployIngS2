import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IVenta } from '../interfaces/venta';
import { InterceptorService } from './interceptor.service';

@Injectable({
  providedIn: 'root'
})
export class VentasService {

  constructor(private _httpClient: HttpClient,
    private interceptor: InterceptorService) { }

  listarVentas():Observable<any[]>{
    return this._httpClient.get<IVenta[]>(`${environment.API_URL}/sale/detail/`,{ headers: this.interceptor.getHeaders()});
  }
}
