import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { IJWTResponse } from '../interfaces/jwt.interface';
import { CookieService } from 'ngx-cookie-service';
import { User } from '../interfaces/usuario';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(
    private httpClient: HttpClient,
    private cookieService: CookieService
  ) {}


  authToken(user: User): Observable<IJWTResponse> {
    return this.httpClient.post<IJWTResponse>(
      `${environment.API_URL}/auth/auth/login/`,
      user, {headers:this.getHeaders()}
    );
  }

  deleteToken(id: string): Observable<any> {
    return this.httpClient.post(`${environment.API_URL}/auth/auth/logout/`, 
    { user: id}, {headers:this.getHeaders()}
    );
  }

  private getHeaders():HttpHeaders{
    return new HttpHeaders({
      'content-type': 'application/json',
      Authorization: `Bearer ${this.cookieService.get('access')}`,
    });
  }
}
