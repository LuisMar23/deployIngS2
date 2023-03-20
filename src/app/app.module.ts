import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CookieService } from 'ngx-cookie-service';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AdminGuard } from './core/guards/admin.guard';
import { AuthModule } from './modules/auth/auth.module';
import { HomeModule } from './modules/home/home.module';
import { InventarioModule } from './modules/inventario/inventario.module';
import { BrowserAnimationsModule, NoopAnimationsModule } from '@angular/platform-browser/animations';
import { StoreModule } from '@ngrx/store';


@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HomeModule,
    AuthModule,
    InventarioModule,
    HttpClientModule,
    BrowserAnimationsModule,
    NoopAnimationsModule,
    // StoreModule.forRoot({}, {}),
  ],
  providers: [CookieService, AdminGuard],
  bootstrap: [AppComponent],
})
export class AppModule {}
