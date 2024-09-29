import React from 'react'
import { useState } from 'react'
import Title from './Title'
function Controller(props) {
  const [isLoadding, setIsLoading] = useState(false);
  const [message, setMessage] = useState<any[]>([]);

  const createBlobUrl = (data: any) => {};

  const handleStop = async() => {};


  return (    
       <div className="h-screen overflow-y-hidden">
        <Title setMessage={setMessage}/>
          <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
           
            paceholder
          </div>
       </div>    
  )
}


export default Controller

