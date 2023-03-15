import { IUsuario } from './usuario';
export interface IJWTResponse{
    access:string,
    refresh:string,
    user:IUsuario
}