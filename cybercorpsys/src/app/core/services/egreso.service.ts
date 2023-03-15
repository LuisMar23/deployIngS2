import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { CookieService } from 'ngx-cookie-service';
@Injectable({
  providedIn: 'root',
})
export class EgresoService {
  constructor(
    private _httpClientService: HttpClient,
    private _cookieService: CookieService
  ) {}

  guardarDetalleEgreso(detalleEgreso: any): Observable<any> {
    return this._httpClientService.post(
      `${environment.API_URL}/almacen/egreso/`,
      detalleEgreso,
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
