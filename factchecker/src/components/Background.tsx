import React from "react";

const Background = () => {
  return (
    <div className="">
      <div className="bg-black opacity-60 h-full w-full absolute -z-10"></div>
      <div className="-z-20 w-full absolute h-screen blur-sm bg-zinc-600">
        <div className="text-2xl lg:text-7xl md:text-4xl   h-full font-sans font-extrabold text-white flex justify-center items-center">
          <span className="mt-2">Chat With Website</span>
        </div>
      </div>
    </div>
  );
};

export default Background;
