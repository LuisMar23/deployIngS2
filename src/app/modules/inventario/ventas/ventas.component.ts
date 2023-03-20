import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { ISede } from 'src/app/core';
import { IVenta } from 'src/app/core/interfaces/venta';
import { VentasService } from 'src/app/core/services/ventas.service';

@Component({
  selector: 'app-ventas',
  templateUrl: './ventas.component.html',
  styleUrls: ['./ventas.component.css']
})
export class VentasComponent implements OnInit,AfterViewInit {
  displayedColumns:string[]=['id','serial_number','price','buy_price','sale_tax','saleTotal','date_created','producto','is_active','opciones']
  private listaVentas!:IVenta[];
 
  dataSource = new MatTableDataSource<IVenta>(this.listaVentas);
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private ventaService:VentasService) { }

  ngOnInit(): void {
    this.listarVentas();
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  listarVentas(){
    this.ventaService.listarVentas().subscribe((resp:IVenta[])=>{
      this.dataSource.data=resp;
    });
  }
}
