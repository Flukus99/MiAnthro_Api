const express= require('express');
const {spawn}=require('child_process');
const multer=require("multer");
const cors= require("cors")

const fs=require("fs");
const app=express();
const PORT= process.env.PORT || 8080;
const date=Date.now()
const whitelist=["http://localhost:4200","http://mi-anthro.vercel.app"]

const storage=multer.diskStorage({
    destination: 'uploads/',
    filename: function(req,file,cb){
       

        cb("","libro"+date+".csv");
    }
})

const upload=multer({
    storage:storage
})

app.use(cors({
    origin:[whitelist]
}));

app.post("/files/:id",upload.single('data'),(req,res)=>{
    
    
   const dataPython=spawn('python',['index.py',date,req.params.id]);
   let data1
   dataPython.stdout.on('data',function(data){
       data1 +=data.toString()
   })
   dataPython.on('close',(code)=>{
       
   })
   dataPython.stdin.end()
  res.json({
      message:"todo va bien",
      
  })
})



app.get('/descarga',async(req , res)=>{

        
      res.download(__dirname+"/Libro"+date+".csv/","libro.csv",(err)=>{
        if(err){
            console.log(err)
        }else{
            
            eliminar(__dirname+"/Libro"+date+".csv");
            eliminar(__dirname+"/uploads/libro"+date+".csv")   
    
        }
      
    })
    
    
})




app.get('/funciona',(req , res)=>{

        
    res.send("funciona")
  
  
})
  







app.listen(PORT, ()=>console.log("funciona escuchando en el puerto 3000"))


function eliminar(ruta){
    fs.unlink(ruta,(error)=>{
        if(error){
            console.error(error);
            console.log("filed deleted :(")
        }
    })
}


