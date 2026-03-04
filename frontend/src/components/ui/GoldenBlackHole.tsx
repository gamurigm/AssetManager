"use client";

import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Sparkles } from '@react-three/drei';
import * as THREE from 'three';

// ─── Accretion Disk (golden smooth torus cloud) ─────────────────────
const PARTICLE_COUNT = 3000;
const RING_R = 3.2;
const TUBE_R = 1.0;

const diskParticles = Array.from({ length: PARTICLE_COUNT }, () => {
    const u = Math.random() * Math.PI * 2;
    const v = Math.random() * Math.PI * 2;
    const x = (RING_R + TUBE_R * Math.cos(v)) * Math.cos(u);
    const y = TUBE_R * Math.sin(v) * 0.08; // ultra-flat disk
    const z = (RING_R + TUBE_R * Math.cos(v)) * Math.sin(u);
    const distance = Math.sqrt(x * x + z * z);
    const speed = (8 / distance) * (Math.random() * 0.4 + 0.6);
    const scale = Math.random() * 0.6 + 0.4;
    return { basePosition: new THREE.Vector3(x, y, z), speed, scale, distance };
});

function AccretionDisk() {
    const groupRef = useRef<THREE.Group>(null);
    const meshRef = useRef<THREE.InstancedMesh>(null);

    useFrame((state) => {
        if (!groupRef.current || !meshRef.current) return;
        const t = state.clock.getElapsedTime();

        // Gentle tilt breathing
        groupRef.current.rotation.y = t * 0.12;
        groupRef.current.rotation.x = 0.35 + Math.sin(t * 0.15) * 0.03;

        const dummy = new THREE.Object3D();
        diskParticles.forEach((p, i) => {
            const angle = Math.atan2(p.basePosition.z, p.basePosition.x) + t * p.speed * 0.3;
            const r = p.distance;
            const yWarp = Math.sin(t * 1.5 + r * 1.2) * 0.06;

            dummy.position.set(Math.cos(angle) * r, p.basePosition.y + yWarp, Math.sin(angle) * r);
            const pulse = (Math.sin(t * 3 + i * 0.01) * 0.3 + 0.7) * p.scale;
            dummy.scale.setScalar(pulse);
            dummy.updateMatrix();
            meshRef.current?.setMatrixAt(i, dummy.matrix);

            // Warm gradient: white-hot center → gold → deep orange edge
            const color = new THREE.Color();
            const nd = Math.max(0, Math.min(1, (r - 2.2) / 3.0));
            color.lerpColors(new THREE.Color('#fffbe6'), new THREE.Color('#d4af37'), nd);
            color.lerp(new THREE.Color('#cc5500'), nd * nd);
            meshRef.current?.setColorAt(i, color);
        });

        meshRef.current.instanceMatrix.needsUpdate = true;
        if (meshRef.current.instanceColor) meshRef.current.instanceColor.needsUpdate = true;
    });

    return (
        <group ref={groupRef}>
            <instancedMesh ref={meshRef} args={[undefined, undefined, PARTICLE_COUNT]}>
                <sphereGeometry args={[0.03, 6, 6]} />
                <meshStandardMaterial
                    toneMapped={false}
                    emissive="#d4af37"
                    emissiveIntensity={2.5}
                    transparent
                    opacity={0.85}
                    blending={THREE.AdditiveBlending}
                    depthWrite={false}
                />
            </instancedMesh>
        </group>
    );
}

// ─── Expanding Harmonic Waves ───────────────────────────────────────
function ExpandingWaves() {
    const wavesRef = useRef<THREE.Group>(null);
    const WAVE_COUNT = 5;

    useFrame((state) => {
        if (!wavesRef.current) return;
        const t = state.clock.getElapsedTime();
        wavesRef.current.children.forEach((ring, i) => {
            const phase = (t * 0.4 + i * (Math.PI * 2 / WAVE_COUNT)) % (Math.PI * 2);
            const progress = phase / (Math.PI * 2); // 0 → 1
            const scale = 2.5 + progress * 6;
            ring.scale.set(scale, scale, scale);
            (ring as THREE.Mesh).material = (ring as THREE.Mesh).material as THREE.MeshBasicMaterial;
            ((ring as THREE.Mesh).material as THREE.MeshBasicMaterial).opacity = (1 - progress) * 0.25;
        });
    });

    return (
        <group ref={wavesRef} rotation={[Math.PI / 2 + 0.35, 0, 0]}>
            {Array.from({ length: WAVE_COUNT }).map((_, i) => (
                <mesh key={i}>
                    <ringGeometry args={[0.98, 1.0, 128]} />
                    <meshBasicMaterial
                        color="#d4af37"
                        side={THREE.DoubleSide}
                        transparent
                        opacity={0}
                        blending={THREE.AdditiveBlending}
                        depthWrite={false}
                    />
                </mesh>
            ))}
        </group>
    );
}

// ─── Distant Stars (subtle, sparse, beautiful) ─────────────────────
function DistantStars() {
    const ref = useRef<THREE.Points>(null);
    const COUNT = 1200;

    const [positions, colors, sizes] = useMemo(() => {
        const pos = new Float32Array(COUNT * 3);
        const col = new Float32Array(COUNT * 3);
        const sz = new Float32Array(COUNT);
        const c = new THREE.Color();

        for (let i = 0; i < COUNT; i++) {
            // Spherical shell 40–80 units away
            const r = 40 + Math.random() * 40;
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos(2 * Math.random() - 1);
            pos[i * 3] = r * Math.sin(phi) * Math.cos(theta);
            pos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
            pos[i * 3 + 2] = r * Math.cos(phi);

            // Subtle star colors
            const rnd = Math.random();
            if (rnd > 0.85) c.set('#aaddff');       // cool blue
            else if (rnd > 0.5) c.set('#ffffff');    // white
            else if (rnd > 0.2) c.set('#ffe8c0');    // warm yellow
            else c.set('#ffcc88');                    // warm orange
            col[i * 3] = c.r; col[i * 3 + 1] = c.g; col[i * 3 + 2] = c.b;

            sz[i] = Math.random() * 0.8 + 0.1;
        }
        return [pos, col, sz];
    }, []);

    useFrame((state) => {
        if (ref.current) {
            ref.current.rotation.y = state.clock.getElapsedTime() * 0.008;
        }
    });

    return (
        <points ref={ref}>
            <bufferGeometry>
                <bufferAttribute attach="attributes-position" args={[positions, 3]} />
                <bufferAttribute attach="attributes-color" args={[colors, 3]} />
            </bufferGeometry>
            <pointsMaterial size={0.12} vertexColors transparent opacity={0.7} sizeAttenuation />
        </points>
    );
}

// ─── Photon Rings (layered golden glow) ─────────────────────────────
function PhotonRings() {
    const ref = useRef<THREE.Group>(null);

    useFrame((state) => {
        if (ref.current) {
            ref.current.rotation.z = state.clock.getElapsedTime() * 0.05;
        }
    });

    return (
        <group ref={ref} rotation={[Math.PI / 2 + 0.35, 0, 0]}>
            {/* Inner white-hot ring */}
            <mesh>
                <ringGeometry args={[1.82, 2.0, 128]} />
                <meshBasicMaterial color="#ffffff" side={THREE.DoubleSide} transparent opacity={0.7} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>
            {/* Gold ring */}
            <mesh>
                <ringGeometry args={[2.0, 2.25, 128]} />
                <meshBasicMaterial color="#d4af37" side={THREE.DoubleSide} transparent opacity={0.5} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>
            {/* Outer soft glow */}
            <mesh>
                <ringGeometry args={[2.25, 2.8, 128]} />
                <meshBasicMaterial color="#b8860b" side={THREE.DoubleSide} transparent opacity={0.15} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>
        </group>
    );
}

// ─── Main Scene ─────────────────────────────────────────────────────
export default function GoldenBlackHole() {
    return (
        <div className="absolute inset-0 w-full h-full overflow-hidden z-0" style={{ background: '#030308' }}>
            {/* Distant nebula glow via CSS — subtle colored halos */}
            <div className="absolute inset-0 pointer-events-none" style={{
                background: `
                    radial-gradient(ellipse 60% 50% at 15% 20%, rgba(100, 60, 180, 0.08) 0%, transparent 70%),
                    radial-gradient(ellipse 50% 40% at 85% 75%, rgba(40, 80, 180, 0.06) 0%, transparent 70%),
                    radial-gradient(ellipse 70% 60% at 50% 50%, rgba(200, 160, 50, 0.04) 0%, transparent 60%),
                    radial-gradient(ellipse 40% 35% at 80% 15%, rgba(200, 80, 120, 0.05) 0%, transparent 70%)
                `
            }} />

            <Canvas camera={{ position: [0, 2.5, 9], fov: 55 }} gl={{ antialias: true, alpha: false }}>
                <color attach="background" args={['#030308']} />
                <ambientLight intensity={0.15} />
                <pointLight position={[0, 0, 0]} intensity={60} color="#ffd700" distance={15} />

                {/* Distant subtle stars */}
                <DistantStars />

                {/* Expanding harmonic wave pulses */}
                <ExpandingWaves />

                {/* Event Horizon */}
                <mesh>
                    <sphereGeometry args={[1.8, 64, 64]} />
                    <meshBasicMaterial color="#000000" />
                </mesh>

                {/* Photon glow rings */}
                <PhotonRings />

                {/* Golden accretion disk */}
                <AccretionDisk />

                {/* Tiny sparkles — very subtle ambient dust */}
                <Sparkles count={200} scale={12} size={1.5} speed={0.3} opacity={0.2} color="#ffd700" />

                <OrbitControls
                    enableZoom={false}
                    enablePan={false}
                    autoRotate
                    autoRotateSpeed={0.4}
                    maxPolarAngle={Math.PI / 2 + 0.25}
                    minPolarAngle={Math.PI / 2 - 0.35}
                />
            </Canvas>
        </div>
    );
}
