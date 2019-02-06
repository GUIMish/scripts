/** Copyright 2019 GUIMIsh <Mish7913@gmail.com> **/

/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *
 */

Shader "Fur/Fur_Shader" {
    Properties {
        _MainTex("Texture", 2D) = "white" {}
        _NormalMap("NormalMap", 2D) = "normal" {}
        _NormalMapIntensity("NormalMap Intensity", Range (0, 10)) = 1
        _FurTex("Fur Pattern", 2D) = "white" {}

        _FurLength ("Fur Length", Range(0.0, 1)) = 0.5
        _CutOff ("Alpha Cutoff", Range(0, 1)) = 0.5
        _Blur ("Blur", Range(0, 1)) = 0.5
        _Thickness ("Thickness", Range(0, 0.5)) = 0
    }
    SubShader {
        Tags { "RenderType" = "Opaque" }
        CGPROGRAM
        #pragma surface surf Lambert
        struct Input {
            float2 uv_MainTex;
            float2 uv_NormalMap;
        };

        sampler2D _MainTex, _NormalMap;
        float _NormalMapIntensity;

        void surf (Input IN, inout SurfaceOutput o) {
            o.Albedo = tex2D(_MainTex, IN.uv_MainTex).rgb;
            o.Normal = UnpackNormal(tex2D (_NormalMap, IN.uv_NormalMap));
            o.Normal.z = o.Normal.z / _NormalMapIntensity;
        }
        ENDCG
    }
    Fallback "Diffuse"
}
