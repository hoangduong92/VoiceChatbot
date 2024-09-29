import React from "react";
import { useState } from "react";
import axios from "axios";

type TitleProps = {
  setMessage: any;
};

const Title = ({ setMessage }: TitleProps) => {
  const [isResetting, setIsResetting] = useState(false);

  // Reset the conversation
  const resetConversation = async () => {
    setIsResetting(true);

    await axios
      .get("http://localhost:8000/reset") // Gọi đến backend, 8000 là cổng mặc định của backend
      .then((res) => {
        if (res.status === 200) {
          setMessage([]);
        } else {
          console.log("There was an error with the reset API call");
        }
      })
      .catch((err) => {
        console.error(err.message);
      });

    setIsResetting(false);
  };
  return (
    <div className="flex justify-between items-center w-full p-4 bg-gray-500 text-white font-bold shadow">
      <div className="italic">Duongbibo</div>
      <button onClick={resetConversation} className="transition-all duration-300 hover:rotate-180">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={1.5}
          stroke="currentColor"
          className="size-6"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0 3.181 3.183a8.25 8.25 0 0 0 13.803-3.7M4.031 9.865a8.25 8.25 0 0 1 13.803-3.7l3.181 3.182m0-4.991v4.99"
          />
        </svg>
      </button>
    </div>
  );
};

export default Title;
