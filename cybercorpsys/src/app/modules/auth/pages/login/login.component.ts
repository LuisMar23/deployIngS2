import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { IUsuario,IJWTResponse,AuthService } from 'src/app/core';

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
    }, error:(error) => {
      Swal.fire({
        icon: 'error',
        title: 'Error de Sesion',
        text: 'El usuario o contraseña no es correcto!',
      });
    }})
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
