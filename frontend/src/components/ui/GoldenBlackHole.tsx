"use client";

import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Instances, Instance, Environment, Sparkles } from '@react-three/drei';
import * as THREE from 'three';

// Math utils for the accretion disk (torus-like point cloud)
const particleCount = 4000;
const ringRadiusOuter = 4.5;
const ringRadiusInner = 2.5;
const tubeRadius = 1.6;

const particles = Array.from({ length: particleCount }, () => {
    const u = Math.random() * Math.PI * 2;
    const v = Math.random() * Math.PI * 2;
    // Main disk
    const r = Math.random() > 0.3 ? ringRadiusInner : ringRadiusOuter;
    const x = (r + tubeRadius * Math.cos(v)) * Math.cos(u);
    const y = tubeRadius * Math.sin(v) * (Math.random() * 0.1); // Flattened y for disk
    const z = (r + tubeRadius * Math.cos(v)) * Math.sin(u);

    // Closer to center = faster rotation & brighter
    const distance = Math.sqrt(x * x + z * z);
    const speed = (12 / distance) * (Math.random() * 0.5 + 0.5);
    const scale = Math.random() * 1.2 + 0.2;

    return {
        position: new THREE.Vector3(x, y, z),
        basePosition: new THREE.Vector3(x, y, z),
        speed,
        scale,
        distance
    };
});

function AccretionDisk() {
    const groupRef = useRef<THREE.Group>(null);
    const instanceRef = useRef<THREE.InstancedMesh>(null);

    useFrame((state) => {
        if (!groupRef.current || !instanceRef.current) return;

        const time = state.clock.getElapsedTime();

        // Rotate entire accretion disk
        groupRef.current.rotation.y = time * 0.15;
        groupRef.current.rotation.z = Math.sin(time * 0.2) * 0.05 + 0.1;
        groupRef.current.rotation.x = Math.cos(time * 0.1) * 0.05 + 0.3;

        // Animate individual particles
        const dummy = new THREE.Object3D();
        particles.forEach((p, i) => {
            const angleOffset = time * p.speed * 0.4;
            const currentAngle = Math.atan2(p.basePosition.z, p.basePosition.x) + angleOffset;
            const radius = p.distance;

            // Warp effect on Y axis
            const yWarp = Math.sin(time * 3 + p.distance * 2) * 0.15;

            dummy.position.set(
                Math.cos(currentAngle) * radius,
                p.basePosition.y + yWarp,
                Math.sin(currentAngle) * radius
            );

            // Pulse scale
            const pulse = (Math.sin(time * 8 + i) * 0.5 + 0.5) * p.scale;
            dummy.scale.set(pulse, pulse, pulse);

            dummy.updateMatrix();
            instanceRef.current?.setMatrixAt(i, dummy.matrix);

            // Color mapping
            const color = new THREE.Color();
            const normalizedDist = Math.max(0, Math.min(1, (radius - ringRadiusInner + tubeRadius) / (tubeRadius * 3)));

            // Ultra-hot center to cold outer edges
            if (radius < 3.0) {
                color.lerpColors(new THREE.Color('#ffffff'), new THREE.Color('#ffeeaa'), normalizedDist * 2);
            } else {
                color.lerpColors(new THREE.Color('#d4af37'), new THREE.Color('#ff4500'), (normalizedDist - 0.3) * 1.5);
            }

            instanceRef.current?.setColorAt(i, color);
        });

        instanceRef.current.instanceMatrix.needsUpdate = true;
        if (instanceRef.current.instanceColor) {
            instanceRef.current.instanceColor.needsUpdate = true;
        }
    });

    return (
        <group ref={groupRef}>
            <instancedMesh ref={instanceRef} args={[undefined, undefined, particleCount]}>
                <sphereGeometry args={[0.035, 8, 8]} />
                <meshStandardMaterial
                    toneMapped={false}
                    emissive="#ffffff"
                    emissiveIntensity={1.5}
                    transparent
                    opacity={0.9}
                    blending={THREE.AdditiveBlending}
                />
            </instancedMesh>

            {/* Event Horizon (The Black Hole itself) */}
            <mesh>
                <sphereGeometry args={[1.8, 64, 64]} />
                <meshBasicMaterial color="#000000" />
            </mesh>

            {/* Photon Ring 1 (Inner Glowing edge) */}
            <mesh rotation={[Math.PI / 2, 0, 0]}>
                <ringGeometry args={[1.81, 1.95, 128]} />
                <meshBasicMaterial color="#ffffff" side={THREE.DoubleSide} transparent opacity={0.8} blending={THREE.AdditiveBlending} />
            </mesh>

            {/* Photon Ring 2 (Outer Golden edge) */}
            <mesh rotation={[Math.PI / 2, 0, 0]}>
                <ringGeometry args={[1.96, 2.3, 128]} />
                <meshBasicMaterial color="#d4af37" side={THREE.DoubleSide} transparent opacity={0.4} blending={THREE.AdditiveBlending} />
            </mesh>

            {/* Magical Sparkles passing by */}
            <Sparkles count={1000} scale={15} size={3} speed={0.8} opacity={0.5} color="#ffd700" />
            <Sparkles count={500} scale={20} size={5} speed={0.2} opacity={0.8} color="#ffffff" />
        </group>
    );
}

function Starfield() {
    const starsRef = useRef<THREE.Points>(null);
    const starCount = 5000;

    // Generate static stars
    const [positions, colors] = React.useMemo(() => {
        const pos = new Float32Array(starCount * 3);
        const col = new Float32Array(starCount * 3);
        const colorObj = new THREE.Color();

        for (let i = 0; i < starCount; i++) {
            // Spherical distribution
            const r = 30 + Math.random() * 50;
            const theta = 2 * Math.PI * Math.random();
            const phi = Math.acos(2 * Math.random() - 1);

            pos[i * 3] = r * Math.sin(phi) * Math.cos(theta);
            pos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
            pos[i * 3 + 2] = r * Math.cos(phi);

            // Random star colors (blue, white, yellow, orange)
            const randColor = Math.random();
            if (randColor > 0.8) colorObj.setHex(0x88ccff); // Blue-ish
            else if (randColor > 0.4) colorObj.setHex(0xffffff); // White
            else if (randColor > 0.1) colorObj.setHex(0xffddaa); // Yellow-ish
            else colorObj.setHex(0xff8844); // Orange/Red-ish

            col[i * 3] = colorObj.r;
            col[i * 3 + 1] = colorObj.g;
            col[i * 3 + 2] = colorObj.b;
        }
        return [pos, col];
    }, []);

    useFrame((state) => {
        if (starsRef.current) {
            starsRef.current.rotation.y = state.clock.getElapsedTime() * 0.02;
            starsRef.current.rotation.x = state.clock.getElapsedTime() * 0.01;
        }
    });

    return (
        <points ref={starsRef}>
            <bufferGeometry>
                <bufferAttribute attach="attributes-position" args={[positions, 3]} />
                <bufferAttribute attach="attributes-color" args={[colors, 3]} />
            </bufferGeometry>
            <pointsMaterial size={0.15} vertexColors transparent opacity={0.8} sizeAttenuation />
        </points>
    );
}

export default function GoldenBlackHole() {
    return (
        <div className="absolute inset-0 w-full h-full bg-[#050510] overflow-hidden z-0">
            {/* Deep space nebula gradients */}
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-indigo-900/20 via-black to-black" />
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-amber-900/10 via-transparent to-transparent" />

            <Canvas camera={{ position: [0, 3, 12], fov: 60 }} gl={{ antialias: true, alpha: false }}>
                <color attach="background" args={['#020205']} />
                <ambientLight intensity={0.2} />
                <pointLight position={[0, 0, 0]} intensity={80} color="#ffdf00" distance={20} />

                <Starfield />
                <AccretionDisk />

                <OrbitControls
                    enableZoom={false}
                    enablePan={false}
                    autoRotate
                    autoRotateSpeed={0.8}
                    maxPolarAngle={Math.PI / 2 + 0.3}
                    minPolarAngle={Math.PI / 2 - 0.4}
                />
            </Canvas>
        </div>
    );
}
