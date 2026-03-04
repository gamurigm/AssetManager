"use client";

import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Instances, Instance, Environment, Sparkles } from '@react-three/drei';
import * as THREE from 'three';

// Math utils for the accretion disk (torus-like point cloud)
const particleCount = 2000;
const ringRadius = 3.5;
const tubeRadius = 1.2;

const particles = Array.from({ length: particleCount }, () => {
    const u = Math.random() * Math.PI * 2;
    const v = Math.random() * Math.PI * 2;
    // Torus parametric eq
    const x = (ringRadius + tubeRadius * Math.cos(v)) * Math.cos(u);
    const y = tubeRadius * Math.sin(v) * (Math.random() * 0.2); // Flattened y for disk
    const z = (ringRadius + tubeRadius * Math.cos(v)) * Math.sin(u);

    // Closer to center = faster rotation & brighter
    const distance = Math.sqrt(x * x + z * z);
    const speed = (10 / distance) * (Math.random() * 0.5 + 0.5);
    const scale = Math.random() * 0.8 + 0.2;

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
        groupRef.current.rotation.y = time * 0.2;
        groupRef.current.rotation.z = Math.sin(time * 0.5) * 0.05;
        groupRef.current.rotation.x = Math.cos(time * 0.3) * 0.05;

        // Animate individual particles
        const dummy = new THREE.Object3D();
        particles.forEach((p, i) => {
            // Orbital mechanics approximation for individual stars/dust
            const angleOffset = time * p.speed * 0.5;
            const currentAngle = Math.atan2(p.basePosition.z, p.basePosition.x) + angleOffset;
            const radius = p.distance;

            // Warp effect on Y axis
            const yWarp = Math.sin(time * 2 + p.distance) * 0.2;

            dummy.position.set(
                Math.cos(currentAngle) * radius,
                p.basePosition.y + yWarp,
                Math.sin(currentAngle) * radius
            );

            // Pulse scale
            const pulse = (Math.sin(time * 5 + i) * 0.5 + 0.5) * p.scale;
            dummy.scale.set(pulse, pulse, pulse);

            dummy.updateMatrix();
            instanceRef.current?.setMatrixAt(i, dummy.matrix);

            // Color mapping - hotter (brighter/whiter) near the center, golden/orange on edges
            const color = new THREE.Color();
            const normalizedDist = Math.max(0, Math.min(1, (radius - ringRadius + tubeRadius) / (tubeRadius * 2)));
            // Golden standard: Center leans white/yellow, edges lean deep orange/red
            color.lerpColors(new THREE.Color('#ffffff'), new THREE.Color('#d4af37'), normalizedDist);
            color.lerp(new THREE.Color('#ff4500'), Math.pow(normalizedDist, 2));
            instanceRef.current?.setColorAt(i, color);
        });

        instanceRef.current.instanceMatrix.needsUpdate = true;
        if (instanceRef.current.instanceColor) {
            instanceRef.current.instanceColor.needsUpdate = true;
        }
    });

    return (
        <group ref={groupRef} rotation={[0.4, 0, 0]}>
            <instancedMesh ref={instanceRef} args={[undefined, undefined, particleCount]}>
                <sphereGeometry args={[0.04, 8, 8]} />
                <meshStandardMaterial
                    toneMapped={false}
                    emissive="#d4af37"
                    emissiveIntensity={2}
                    transparent
                    opacity={0.8}
                />
            </instancedMesh>

            {/* Event Horizon (The Black Hole itself) */}
            <mesh>
                <sphereGeometry args={[2.0, 64, 64]} />
                <meshBasicMaterial color="#000000" />
            </mesh>

            {/* Photon Ring (Glowing edge around black hole) */}
            <mesh>
                <ringGeometry args={[2.01, 2.15, 64]} />
                <meshBasicMaterial color="#ffd700" side={THREE.DoubleSide} transparent opacity={0.6} blending={THREE.AdditiveBlending} />
            </mesh>

            {/* Magical Sparkles passing by */}
            <Sparkles count={500} scale={12} size={2} speed={0.4} opacity={0.3} color="#ffdf00" />
        </group>
    );
}

export default function GoldenBlackHole() {
    return (
        <div className="absolute inset-0 w-full h-full bg-black overflow-hidden z-0">
            {/* Soft background glow */}
            <div className="absolute inset-0 bg-gradient-to-tr from-orange-900/10 via-black to-yellow-900/10" />

            <Canvas camera={{ position: [0, 2, 8], fov: 60 }} gl={{ antialias: true, alpha: false }}>
                <color attach="background" args={['#000000']} />
                <ambientLight intensity={0.5} />
                <pointLight position={[0, 0, 0]} intensity={50} color="#ffdf00" distance={10} />
                <AccretionDisk />
                <OrbitControls
                    enableZoom={false}
                    enablePan={false}
                    autoRotate
                    autoRotateSpeed={0.5}
                    maxPolarAngle={Math.PI / 2 + 0.2}
                    minPolarAngle={Math.PI / 2 - 0.5}
                />
            </Canvas>
        </div>
    );
}
