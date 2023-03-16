import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { IUsuario,IJWTResponse,AuthService, AlertsService } from 'src/app/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  public form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private cookieService: CookieService,
    private route: Router,
    private _alertService:AlertsService,
  ) {
    this.form = this.fb.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]],
    });
  }

  ngOnInit(): void {}
  login(): void {
    const user:IUsuario = this.form.value;
    this.authService.authToken(user).subscribe({next:(data) => {
      this.saveToken(data);
      this.route.navigate(['/home']);
      //metodo refactorizado Rober Guerrero
    }, error:(error) => this._alertService.alertError("Credenciales incorrectas")});
    this.form.reset();
  }

  private saveToken(resp: IJWTResponse) {
    this.cookieService.set('user', resp.user.username,1,'/');
    this.cookieService.set('id', resp.user.id.toString(), 1, '/');
    this.cookieService.set('access', resp.access, 1, '/');
    this.cookieService.set('refresh', resp.refresh, 1, '/');
    this.cookieService.set('rol', resp.user.usertype, 1, '/');
  }
}
