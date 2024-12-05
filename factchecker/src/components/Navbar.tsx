"use client";

import { redirectHome } from "@/action/redirectHome";
import React from "react";

export const Navbar = () => {
  return (
    <div className="relative flex flex-col">
      <div className="flex top-0 left-0 flex-row fixed w-full z-20 h-14 items-center bg-zinc-900">
        <div
          onClick={async () => {
            await redirectHome();
          }}
          className="text-white text-xl cursor-pointer ml-9 font-extrabold"
        >
          Fact Checker
        </div>
      </div>
    </div>
  );
};
